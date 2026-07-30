from flask import Flask, render_template, request, session, redirect
import mysql.connector

app = Flask(__name__)
app.secret_key = "heritage123"


# Database Connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="AbiNaya@4002",
        database="heritage_db"
    )


# ---------------- SIGN UP ----------------

@app.route('/', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        con = get_connection()
        cur = con.cursor()

        # Check existing email
        cur.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cur.fetchone()

        if user:
            con.close()
            return "Email already exists. Please Login."

        # Insert new user
        cur.execute(
            "INSERT INTO users(name,email,password) VALUES(%s,%s,%s)",
            (name, email, password)
        )

        con.commit()
        con.close()

        # Create Session
        session["name"] = name
        session["email"] = email

        # Go to Home Page
        return render_template("home.html")

    return render_template("signup.html")


# ---------------- LOGIN ----------------

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        con = get_connection()
        cur = con.cursor()

        cur.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )

        user = cur.fetchone()

        con.close()

        if user:
            session["name"] = user[1]
            session["email"] = user[2]

            return render_template("home.html")

        return "Invalid Email or Password"

    return render_template("login.html")


# ---------------- HOME ----------------

@app.route('/home')
def home():

    if "email" not in session:
        return redirect("/login")

    return render_template("home.html")


# ---------------- LOGOUT ----------------

@app.route('/logout')
def logout():

    session.clear()
    return redirect("/login")


#-----------categories----------------

@app.route('/temple')
def temple():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("temple",))
    temples = cur.fetchall()
    con.close()
    return render_template("categories/temple.html", temples=temples)


@app.route('/church')
def church():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("church",))
    churches = cur.fetchall()
    con.close()
    return render_template("categories/church.html", churches=churches)


@app.route('/mosque')
def mosque():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("mosque",))
    mosques = cur.fetchall()
    con.close()
    return render_template("categories/mosque.html", mosques=mosques)


@app.route('/gurudwara')
def gurudwara():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("gurudwara",))
    gurudwaras = cur.fetchall()
    con.close()
    return render_template("categories/gurudwara.html", gurudwaras=gurudwaras)


@app.route('/monastery')
def monastery():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("monastery",))
    monasteries = cur.fetchall()
    con.close()
    return render_template("categories/monastery.html", monasteries=monasteries)


@app.route('/fort')
def fort():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("fort",))
    forts = cur.fetchall()
    con.close()
    return render_template("categories/fort.html", forts=forts)


@app.route('/palace')
def palace():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("palace",))
    palaces = cur.fetchall()
    con.close()
    return render_template("categories/palace.html", palaces=palaces)


@app.route('/monument')
def monument():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("monument",))
    monuments = cur.fetchall()
    con.close()
    return render_template("categories/monument.html", monuments=monuments)


@app.route('/museum')
def museum():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("museum",))
    museums = cur.fetchall()
    con.close()
    return render_template("categories/museum.html", museums=museums)


@app.route('/cave')
def cave():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("cave",))
    caves = cur.fetchall()
    con.close()
    return render_template("categories/cave.html", caves=caves)


@app.route('/archaeological')
def archaeological():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("archaeological",))
    archaeological_sites = cur.fetchall()
    con.close()
    return render_template("categories/archaeological.html", archaeological_sites=archaeological_sites)


@app.route('/tomb')
def tomb():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("tomb",))
    tombs = cur.fetchall()
    con.close()
    return render_template("categories/tomb.html", tombs=tombs)


@app.route('/nationalpark')
def nationalpark():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("nationalpark",))
    national_parks = cur.fetchall()
    con.close()
    return render_template("categories/nationalpark.html", national_parks=national_parks)


@app.route('/wildlife')
def wildlife():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("wildlife",))
    wildlife_sanctuaries = cur.fetchall()
    con.close()
    return render_template("categories/wildlife.html", wildlife_sanctuaries=wildlife_sanctuaries)


@app.route('/birdsanctuary')
def birdsanctuary():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("birdsanctuary",))
    bird_sanctuaries = cur.fetchall()
    con.close()
    return render_template("categories/birdsanctuary.html", bird_sanctuaries=bird_sanctuaries)


@app.route('/hillstation')
def hillstation():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    # DB la "hillstation" and "hill station" rendu spelling um irukura, so rendaiyum check pannurom
    cur.execute(
        "SELECT * FROM heritage_places WHERE category = %s OR category = %s",
        ("hillstation", "hill station")
    )
    hill_stations = cur.fetchall()
    con.close()
    return render_template("categories/hillstation.html", hill_stations=hill_stations)


@app.route('/valley')
def valley():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("valley",))
    valleys = cur.fetchall()
    con.close()
    return render_template("categories/valley.html", valleys=valleys)


@app.route('/waterfall')
def waterfall():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("waterfall",))
    waterfalls = cur.fetchall()
    con.close()
    return render_template("categories/waterfall.html", waterfalls=waterfalls)


@app.route('/beach')
def beach():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("beach",))
    beaches = cur.fetchall()
    con.close()
    return render_template("categories/beach.html", beaches=beaches)


@app.route('/island')
def island():
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM heritage_places WHERE category = %s", ("island",))
    islands = cur.fetchall()
    con.close()
    return render_template("categories/island.html", islands=islands)


#--------------connect category--------------

@app.route('/place/<int:id>')
def place(id):
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute(
        "SELECT * FROM heritage_places WHERE id=%s",
        (id,)
    )
    place = cur.fetchone()
    con.close()
    return render_template(
        "place_details.html",
        place=place
    )


# ---------------- SEARCH ----------------


@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    if not query:
        return redirect('/home')

    con = get_connection()
    cur = con.cursor(dictionary=True)
    try:
        cur.execute(
            """
            SELECT * FROM heritage_places
            WHERE REPLACE(place_name, ' ', '') LIKE %s
               OR REPLACE(state, ' ', '') LIKE %s
               OR REPLACE(category, ' ', '') LIKE %s
            """,
            (f"%{query.replace(' ', '')}%",
             f"%{query.replace(' ', '')}%",
             f"%{query.replace(' ', '')}%")
        )
        results = cur.fetchall()
    finally:
        con.close()

    return render_template("search_results.html", query=query, results=results)


if __name__ == "__main__":
    app.run(debug=True)