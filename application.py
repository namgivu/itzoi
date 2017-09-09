from app import app as application

if __name__ == '__main__':
  #enable error page showed to browser and allow logger.debug() to print
  application.debug = True

  #`debug` auto-reload for code changes and show a debugger in case an exception happened
  application.run(host='0.0.0.0', debug=True, port=5000, threaded=True)
