import os

class RecyclingManager:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(os.getenv('BLOCKCHAIN_NETWORK')))
        with open('blockchain/smart_contracts/RecyclingToken.json') as f:
            contract_abi = json.load(f)['abi']
        self.contract = self.w3.eth.contract(
            address=os.getenv('CONTRACT_ADDRESS'),
            abi=contract_abi
        )
    
    def award_points(self, user_address, amount):
        tx = self.contract.functions.mint(
            Web3.toChecksumAddress(user_address),
            amount
        ).buildTransaction({
            'from': self.w3.eth.accounts[0],
            'nonce': self.w3.eth.getTransactionCount(self.w3.eth.accounts[0])
        })
        signed_tx = self.w3.eth.account.signTransaction(tx, private_key=os.getenv('PRIVATE_KEY'))
        return self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)