import functools
user = {"username": "jose", "access_level": "admin"}


def make_secure(access_level):
 def decorator(func):
  @functools.wraps(func)
  def secure_function(*args, **kwargs):
    if user["access_level"] == access_level:
        return func(*args, **kwargs)
    else:
        return f"No {access_level} permission for user {user['username']}"
  return secure_function
 return decorator  
# cách 1:
# get_admin_password = make_secure(get_admin_password) 
# cách 2: tương tự loại bỏ get_admin_password = make_secure(get_admin_password) 
# @make_secure
# def get_password(panel):
#     if panel == "admin":
#        return "1234"
#     elif panel == "billing":
#         return "super_secure_password"
# print(get_password("billing"))


@make_secure("admin")
def get_admin_passeword():
  return "admin: 1234"


@make_secure("guest")
def get_dashboard_password():
  return "user: user_password" 


print(get_admin_passeword())
