import motor.motor_asyncio
from config.config_reader import config
client = motor.motor_asyncio.AsyncIOMotorClient(config.base_token.get_secret_value())

class Database:
    def __init__(self, db_name='OutDiceTG', url=f'{config.base_token.get_secret_value()}'):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(url)
        self.db = self.client[db_name]
        self.users_collection = self.db["users"]
    
    async def register_user(self, user_id):
        user_data = await self.users_collection.find_one({"user_id": user_id})
        if not user_data:
            new_user = {
                "user_id": user_id,
                "balance_TON": 0.0,
                "balance_NOT": 0.0,
                "game_balance": "TON"
            }
            await self.users_collection.insert_one(new_user)
            return True, None
        return False, 'User already registered'
    
    def get_user_balance(self, user_id):
        user_data = self.users_collection.find_one({"user_id": user_id})
        if user_data:
            return user_data["balance_TON"], user_data["balance_NOT"]
        return None, None

    def update_user_balance(self, user_id, balance_TON=None, balance_NOT=None):
        if balance_TON is not None:
            self.users_collection.update_one({"user_id": user_id}, {"$set": {"balance_TON": balance_TON}})
        if balance_NOT is not None:
            self.users_collection.update_one({"user_id": user_id}, {"$set": {"balance_NOT": balance_NOT}})
