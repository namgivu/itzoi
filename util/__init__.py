from flask import session


def hasLoggedIn():
  return True if 'authInfo' in session else False


def markAsLoggedIn(user=None):
  session['authInfo'] = dict(
    user = dict(username='admin', password='admin')
  )

#region others
pass


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
