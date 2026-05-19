#dictionary is a collection of key value pairs
#it is mutable but keys in dictionary are immutable that means we can change the value of a key but we cannot change the key itself
#the key must be unique in a dictionary but the value can be duplicate
#it uses curly braces {} to define a dictionary and each key value pair is separated by a colon : and each pair is separated by a comma ,
#we can access the value of a key by using the key name in square brackets [] or by using the get() method

#creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict) #output: {'name': 'John', 'age': 30, 'city': 'New York'}


#accessing values in a dictionary
print(my_dict["name"]) #output: John
print(my_dict.get("age")) #output: 30     


#if we use duplicate keys in a dictionary, the last value will overwrite the previous value
my_dict = {"name": "John", "age": 30, "city": "New York", "name": "Jane"}
print(my_dict) #output: {'name': 'Jane', 'age': 30, 'city': 'New York'} here m=name john chnaged to jane because of duplicate key name


#modifying values in a dictionary updating the value of a key in a dictionary
my_dict["age"] = 35
print(my_dict) #output: {'name': 'Jane', 'age': 35, 'city': 'New York'} here age value changed from 30 to 35


#adding new key value pair to a dictionary
my_dict["country"] = "USA"
print(my_dict) #output: {'name': 'Jane', 'age': 35, 'city': 'New York', 'country': 'USA'} here new key value pair country: USA added to the dictionary


#removing key value pair from a dictionary
del my_dict["city"]
print(my_dict) #output: {'name': 'Jane', 'age': 35, 'country': 'USA'} here key value pair city: New York removed from the dictionary


#dictionary methods
#keys() method returns a view object that contains the keys of the dictionary
print(my_dict.keys()) #output: dict_keys(['name', 'age', 'country']) here it returns the keys of the dictionary
#values() method returns a view object that contains the values of the dictionary
print(my_dict.values()) #output: dict_values(['Jane', 35, 'USA'])
#items() method returns a view object that contains the key value pairs of the dictionary as tuples
print(my_dict.items()) #output: dict_items([('name', 'Jane'), ('age', 35), ('country', 'USA')]) here it returns the key value pairs of the dictionary as tuples


#shallow copy of a dictionary
my_dict_copy = my_dict.copy()
print(my_dict_copy) #output: {'name': 'Jane', 'age': 35, 'country': 'USA'} here it creates a shallow copy of the dictionary
#deep copy of a dictionary
import copy
my_dict_deep_copy = copy.deepcopy(my_dict)
print(my_dict_deep_copy) #output: {'name': 'Jane', 'age': 35, 'country': 'USA'} here it creates a deep copy of the dictionary 
#meaning that it creates a new dictionary with the same key value pairs but if we change the value of a key in the original dictionary it will not affect the deep copy of the dictionary


#iterating through a dictionary
for key in my_dict:
    print(key) #output: name age country here it iterates through the keys of the dictionary
for value in my_dict.values():
    print(value) #output: Jane 35 USA here it iterates through the values of the dictionary
for key, value in my_dict.items():
    print(key, value) #output: name Jane age 35 country USA here it iterates through the key value pairs of the dictionary


#nested dictionary is a dictionary that contains another dictionary as a value
nested_dict = {
    "person1": {"name": "John", "age": 30}, 
    "person2": {"name": "Jane", "age": 25}
    }
print(nested_dict) #output: {'person1': {'name': 'John', 'age': 30}, 'person2': {'name': 'Jane', 'age': 25}} here it creates a nested dictionary


#iterating through a nested dictionary
for person, details in nested_dict.items():
    print(person) #output: person1 person2 here it iterates through the keys of the nested dictionary
    for key, value in details.items():
        print(key, value) #output: name John age 30 name Jane age 25 here it iterates through the key value pairs of the nested dictionary



