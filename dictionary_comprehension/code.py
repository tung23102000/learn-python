users = [
    (0, "Bob", "password"),
    (1, "Rolf","1234"),
    (2, "Jose", "longp4ssword")
    
]

username_mapping = { user[1]: user for user in users} #this is a dictionary username_mapping 


username_input = input("Enter your ussername: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]
# điều này có nghĩa là ví dụ: nếu username_input="Bob"  => username_mapping["Bob"] = (0,'Bob','password') => _,username, password = (dấu _ chỉ bỏ qua giá trị đó k sử dụng tới chỉ lấy username, password) 
# => username = "Bob", password = "password"

if password_input == password:
     print("your detail is correct")
else: 
    print("your detail is incorrect")
