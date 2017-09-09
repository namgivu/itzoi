def hasLoggedIn():
  return False
  return True


#region others
pass


# def getAuthInfo():
#   from app import session
#   return session.get('authInfo') #get session key ignoring if not exists ref. http://stackoverflow.com/a/28926347/248616
#
#
#
# def currentUser():
#   from app import session
#   try:
#     return session['authInfo']['user']
#   except:
#     return None
#
#
# def markAsLoggedIn(user):
#   from app import session
#   session['authInfo'] = dict(
#     user = user.toDict()
#   )
#
#
# def requireValueFromRequest(request, field, allowEmpty=False):
#   value = request.values.get(field)
#   if value: return value
#
#   if not value: #value not found
#     #region raise error if required i.e. allowEmpty=False
#     if not allowEmpty:
#       raise Exception('Param `%s` is required' % field)
#
#     else: #return None when empty is a need, do it
#       return None
#
#     pass
#     #endregion raise error if required i.e. allowEmpty=False

pass
#endregion others
