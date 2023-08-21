"""
Status code and message .
------------------------------
Format of a custom code :
"operation-name":{
  "code":integer (use 4 number digit),
  "message": string (text to describe the code)
}
"""

custom_code={
  
  "login-success":{
    "code":2000,
    "msg":"login is successfull"
  },
  
  "user-create-success":{
    "code":2001,
    "msg":"user is created"
  },
  
  "username-invalid":{
    "code":3000,
    "msg":"username is not valid"
  },

  "username-empty":{
    "code":3001,
    "msg":"username is required"
  },
    
  "email-empty":{
    "code":3002,
    "msg":"email is required"
  },
    
  "email-invalid":{
    "code":3003,
    "msg":"email is not valid"
  },
  
  "password-empty":{
    "code":3002,
    "msg":"password is required"
  },
    
  "password-invalid":{
    "code":3003,
    "msg":"password is not valid"
  },    
  
  "email-password-invalid":{
    "code":3004,
    "msg":"email or password is incorrect"
  },   
  
  "token-invalid":{
    "code":3005,
    "msg":"token is not valid"
  },
  
  "email-already-exit":{
    "code":3006,
    "msg":"email is already exist"
  },
  
}