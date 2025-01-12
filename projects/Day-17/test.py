class User:
    
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.name = user_name
        self.account_type='default'
        self.followers=0
        self.following=0
        
    def level_up(self):
        self.account_type='premium'
        return self.account_type
    
    def follow(self,user):
        self.following+=1
        user.followers+=1
        print(f'{self.name} started following {user.name}.')

user_1=User(101,'Rekha')
user_2=User(102,'Sravan')

user_1.follow(user_2)
print(f'user 1 following: {user_1.following}')
print(f'user 2 following: {user_2.following}')
print(f'user 1 followers: {user_1.followers}')
print(f'user 2 followers: {user_2.followers}')