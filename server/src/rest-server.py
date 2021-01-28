from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

import mysql.connector as mysql
import os

''' Environment Variables '''
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

''' Collection Route to GET Students '''
def get_students(req):
  # Connect to the database and retrieve the students
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select id, first_name, last_name, email, age from TestUsers;")
  records = cursor.fetchall()

  # Format the result as key-value pairs
  response = {}
  for index, row in enumerate(records):
    response[index] = {
      "id": row[0],
      "first_name": row[1],
      "last_name": row[2],
      "email": row[3],
      "age": row[4]
    }

  return response

''' Instance Route to GET Student '''
def get_student(req):
  # Retrieve the route argument (this is not GET/POST data!)
  the_id = req.matchdict['student_id']

  # Connect to the database and retrieve the student
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select * from TestUsers where id='%s';" % the_id)
  record = cursor.fetchone()
  db.close()

  if record is None:
    return ""

  # Format the result as key-value pairs
  response = {
    'id':         record[0],
    'first_name': record[1],
    'last_name':  record[2],
    'email':      record[3],
    'age':        record[4],
    'datetime':   record[5].isoformat()
  }

  return response


''' Route Configurations '''
if __name__ == '__main__':
  with Configurator() as config:

    config.add_route('get_students', '/students')
    config.add_view(get_students, route_name='get_students', renderer='json')

    config.add_route('get_student', '/student/{student_id}')
    config.add_view(get_student, route_name='get_student', renderer='json')

    app = config.make_wsgi_app()

  server = make_server('0.0.0.0', 6543, app)
  print('Web server started on: http://0.0.0.0:6543')
  server.serve_forever()
