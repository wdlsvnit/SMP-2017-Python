from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
from datetime import datetime

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
@login_required
def index():
    info=db.execute("SELECT symbol,name,shares,price,total FROM portfolio WHERE id=:id",\
                    id=session["user_id"])

    cash = db.execute("SELECT cash FROM users WHERE id = :id", \
                    id=session["user_id"])

    total= unusd(cash[0]["cash"])

    for infos in info:
        total += unusd(infos["total"])

    return render_template("index.html",stocks=info,cash=cash[0]["cash"],total=usd(total))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""
    if request.method=="GET":
        return render_template("buy.html")

    else:

        if not request.form.get("symbol"):
            return apology("must provide symbol")

        elif not request.form.get("shares") :
            return apology("must provide number of shares")

        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("must provide an integer")

        if (shares < 0) :
            return apology("Shares must be positive integer")

        stock=lookup(request.form.get("symbol"))

        if stock == None :
            return apology("Invalid Symbol")

        else:
            money = db.execute("SELECT cash FROM users WHERE id = :id", \
                            id=session["user_id"])
            if not money :
                return apology("Not present")
        # check if enough money to buy
            if (unusd(money[0]["cash"]) < stock["price"] * shares):
                return apology("Not enough money")

            user_shares = db.execute("SELECT shares FROM portfolio \
                           WHERE id = :id AND symbol=:symbol", \
                           id=session["user_id"], symbol=stock["symbol"])

            if not user_shares:
                ins=db.execute("INSERT INTO portfolio (name, shares, price, total, symbol, id) \
                        VALUES(:name, :shares, :price, :total, :symbol, :id)", \
                        name=stock["name"], shares=shares, price=usd(stock["price"]), \
                        total=usd(shares * stock["price"]), \
                        symbol=stock["symbol"], id=session["user_id"])
                if not ins:
                    return apology("HAHAH")

            else:
                shares_total = user_shares[0]["shares"] + shares

                up=db.execute("UPDATE portfolio SET shares=:shares \
                        WHERE id=:id AND symbol=:symbol", \
                        shares=shares_total, id=session["user_id"], \
                        symbol=stock["symbol"])

                if not up:
                    return("HUHUHU")

             # update history
            db.execute("INSERT INTO history (symbol, shares, price, id,transacted) \
                    VALUES(:symbol, :shares, :price, :id,:transacted)", \
                    symbol=stock["symbol"], shares=shares, \
                    price=usd(stock["price"]), id=session["user_id"],\
                    transacted=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            # update user cash
            db.execute("UPDATE users SET cash =:purchase WHERE id = :id", \
                    id=session["user_id"], \
                    purchase=usd(unusd(money[0]["cash"])-(stock["price"] * shares)))

        return redirect(url_for("index"))


@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    histories=db.execute("SELECT * FROM history WHERE id=:id ORDER BY transacted DESC",id=session["user_id"])

    if not histories:
        return render_template("history.html")

    return render_template("history.html",histories=histories)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method=="GET":
        return render_template("quote.html")


    else :
        if not request.form.get("symbol"):
            return apology("Missing symbol")

        stock=lookup(request.form.get("symbol"))

        if stock == None :
            return apology("Invalid Symbol")

        else :
            return render_template("quoted.html",name=stock["name"],symbol=stock["symbol"],price=usd(stock["price"]))


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""

    if request.method == "POST":

        if not request.form.get("username"):
            return apology("Must provide username")


        elif not request.form.get("password"):
            return apology("Must provide password")

        elif not request.form.get("password(again)"):
            return apology("Must provide confirmation password")

        # ensure password and verified password is the same
        elif request.form.get("password") != request.form.get("password(again)"):
            return apology("password doesn't match")

        # insert the new user into users, storing the hash of the user's password
        result = db.execute('''INSERT INTO users (username, hash,cash)
                             VALUES(:username, :hash,:cash)''',
                             username=request.form.get("username"),
                             hash=pwd_context.hash(request.form.get("password")),
                             cash=usd(10000.00))

        if not result:
            return apology("Username already exist")

        # remember which user has logged in
        session["user_id"] = result

        # redirect user to home page
        return redirect(url_for("index"))

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""

    if request.method=="GET":
        return render_template("sell.html")

    else:
        if not request.form.get("symbol"):
            return apology("must provide symbol")

        elif not request.form.get("shares"):
            return apology("must provide number of shares")

        try:
            share = int(request.form.get("shares"))
        except ValueError:
            return apology("must provide an integer")

        if (share < 0) :
            return apology("Shares must be positive integer")

        stock=lookup(request.form.get("symbol"))

        if stock == None :
            return apology("Invalid Symbol")

        p_share = db.execute("SELECT shares FROM portfolio WHERE name=:name AND id=:id",name=stock["name"],id=session["user_id"])

        if p_share==None:
            return appology("U own no such share")

        if int(p_share[0]["shares"]) < share :
            return apology("Not enough stock")

        newShare=int(p_share[0]["shares"])-share

        cash = db.execute("SELECT cash FROM users WHERE id = :id", \
                        id=session["user_id"])

        newCash=usd(unusd(cash[0]["cash"]) + share*stock["price"])

        db.execute("UPDATE users SET cash=:cash WHERE id=:id",cash=newCash,id=session["user_id"])

        if newShare==0:
            db.execute("DELETE FROM portfolio WHERE id=:id AND name=:name",id=session["user_id"],name=stock["name"])
        else :
            db.execute("UPDATE portfolio SET shares=:shares,total=:total WHERE name=:name AND id=:id" ,\
                    shares=newShare,total=usd(newShare*stock["price"]),name=stock["name"],id=session["user_id"])

        db.execute("INSERT INTO history (symbol, shares, price, id,transacted) \
                VALUES(:symbol, :shares, :price, :id,:transacted)", \
                symbol=stock["symbol"], shares=(-share), \
                price=usd(stock["price"]), id=session["user_id"],\
                transacted=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return redirect(url_for("index"))

@app.route("/resetPass", methods=["GET", "POST"])
@login_required
def resetPass():
    """ Reset password """

    if request.method=="GET":
        return render_template("resetPass.html")

    else:
        # ensure oldpass was submitted
        if not request.form.get("oldPassword"):
            return apology("Must provide old password")

        # ensure password was submitted
        elif not request.form.get("newPassword"):
            return apology("Must provide new password")

        elif not request.form.get("password(again)"):
            return apology("Must provide confirmation password")

        extPass=db.execute("SELECT hash FROM users WHERE id=:id",id=session["user_id"])

        oldPass=request.form.get("oldPassword")

        #For dbg
        #print(extPass[0]["hash"])
        #print(oldPass)

        #if oldPass!=extPass[0]["hash"]:
            #return apology("Check current password, typed incorrectly")

        if pwd_context.verify(oldPass,extPass[0]["hash"]) == False :
            return apology("Check current password, typed incorrectly")

        elif request.form.get("newPassword") != request.form.get("password(again)"):
                return apology("New Password doesn't match")


        else :
            status=db.execute("UPDATE users SET hash=:hash WHERE id=:id",\
                    hash=pwd_context.hash(request.form.get("newPassword")),
                    id=session["user_id"])

            if not status:
                return render_template("resetStatus.html",status="Failed")

            else:
                return render_template("resetStatus.html",status="Success")
