from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str

# if __name__ == "__main__":
#     # This block only runs when the script is executed directly
#     thing = Creature(
#         name='yeti', country='CN', area='Himalayas',
#         description='Hirsute Himalayan', aka='Abominable Snowman')
#     print("Name is", thing.name)