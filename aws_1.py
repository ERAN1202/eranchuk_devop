#!/bin/python3

import boto3
from time import sleep


def deploy_instance():
    ec2 = boto3.resource('ec2')
    instances = ec2.create_instances(
        ImageId=input("Enter machine ID:\n"),
        Mincount = 1,
        MaxCount = int(input("How many instances?\n")),
        InstanceType=input("Which type of instance?\n",
        KeyName='eranchuk_devop'

)

def describe_instances():
    client = botot3.client('ec2')
    response = client.describe_instances()
    for r in response['Reservaions']:
       for i in r['Instances']:
            print("ID: " + i['InstanceId'] + "\nIP Address: " + i['PrivatecIpAddress'] + "\n------------------------------\n")
 
def destroy_instance():
    instances=input("enter the IDs of the instances that you want to terminate:")
    ids= [instances]
    ec2 = boto3.resource('ec2')
    
    ec2.instances.filter(InstanceIds = ids).terminate()

def stop_instance():
    instances=input("enter the IDs of the instances that you want to stop?:")$
    ids= [instances]
    ec2 = boto3.resource('ec2')

    ec2.instances.filter(InstanceIds = ids).stop()

def start_instance():
    instances=input("enter the IDs of the instances that you want to stop?:")$
    ids= [instances]
    ec2 = boto3.resource('ec2')

    ec2.instances.filter(InstanceIds = ids).start()

def menu():
    while(True):
        choice=input("Menu:\n1.Describe EC2 \n2.Deploy EC2  \n3.Terminate EC2 \n4.Stop EC2 n\5.Start EC2 \n"
        if(choice=="1"):
            print("Now we will show your Instances:...\n")
     	    sleep(3)
            describe_instances()
        elif(choice=="2"):
            deploy_instance()
        elif(choice=="3"):
            destroy_instance()
        elif(choice=="4"):
            stop_instance()
        elif(choice="5"):
            start_instance()
        else:
            print("Enter 1-5 only!!!...\n")
            continue
        exit=input("Do you want to exit? yes/no\n")
        if(exit=="yes")
            print("Bye...\n")
            break


menu()
