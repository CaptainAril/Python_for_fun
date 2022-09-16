#!/usr/bin/env python3

# # Ask to enter any email
email = input("Enter your email: ")

# remove any unnecessary white spaces
email = email.strip()

# Get the index of @
slicer_index = email.index('@')

# detch the user name by string slicing
username = email[:slicer_index]

# fetch the domain name by string slicing
domain_name = email[slicer_index+1:]

# print the result seperately
print("Your user name is ", username," and your domain is ",domain_name)

#clcoding.com
