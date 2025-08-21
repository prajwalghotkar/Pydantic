# type validation
def insert_paitent_data(name:str,age:int):

    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print('insert into database')
    else:
        raise TypeError('Invalid data types provided for name or age')
insert_paitent_data('Prawjal','24')
  