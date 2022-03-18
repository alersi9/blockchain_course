# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 14:46:41 2022

@author: alexi
"""

#Module 1 - Create a blockchain

# Para instalar:
# Flask==1.1.2: pip install Flask==1.1.2
# Cliente HTTP Postman: https://www.postman.com/downloads/

# Import the libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Create the blockchain
class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
        def create_block(self, proof, previous_hash):
            block = {'index' : len(self.chain)+1,
                     'timestamp' : str(datetime.datetime.now()), # Converted to string for json
                     'proof' : proof,
                     'previous_hash' : previous_hash}
            
            self.chain.append(block)
            return block
        
        def get_previous_block(self):
            return self.change[-1]  # First position starting by the end 
        
        def proof_of_work(self, previous_proof):
            new_proof = 1
            check_proof = False
            while check_proof is False:
                hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest() # We need binary string (encode)
                # Now we need to check if the new_proof solves the cryptographic equation: '0000...'
                if hash_operation[:4] == '0000':
                    check_proof = True
                else:
                    new_proof += 1
            return new_proof
                    
            

# Part 2 - Mining of a block