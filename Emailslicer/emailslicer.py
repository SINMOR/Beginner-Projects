def email_slicer():
      while True:
            print('Good Morning welcome to your Email slicer program ')
            email = input('Enter your email:')
            (username,domain)=email.split('@')
            (domain,extension)=domain.split('.')
            print(f'This is my username:{username}')
            print(f'This is my domain:{domain}')
            print(f'This is my extension:{extension}')
      

email_slicer()
      
    
    