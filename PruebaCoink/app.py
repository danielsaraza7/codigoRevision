from flask import Flask,render_template,request,redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='usuario'
mysql.init_app(app)


@app.route('/')
def index():

    sql="SELECT * FROM `usuarios`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    usuarios =cursor.fetchall()
    print(usuarios)


    conn.commit()

    return  render_template ('empleados/index.html',usuarios=usuarios)




@app.route('/create')
def create():
   
     return render_template('empleados/create.html')

@app.route('/store', methods=['POST'])
def storage():
    _nombre=request.form ['txtNombre']
    _correo=request.form ['txtCorreo']
    _ciudad=request.form ['txtCiudad']

   
    sql="INSERT INTO `usuarios` (`id`, `nombre`, `email`, `ciudad`) VALUES (NULL, %s, %s, %s);"
   
    datos=(_nombre,_correo,_ciudad)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

    return  render_template ('empleados/index.html')


if __name__ =="__main__":
   app.run( debug=True)