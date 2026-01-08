from fastapi import APIRouter

from app.models.item_model import ItemModel

# Check users.py for relevant comments

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

# Temporary DB of evil items
item_database = {
    1: ItemModel(
        id=1,
        name="Embarrassing Moment Rememberizer",
        description="Reminds victims of the incident from kindergarten",
        inventory=5,
        price=49.99
    ),
    2: ItemModel(
        id=2,
        name="Cauliflowerizer",
        description="Turns mashed potatoes into mashed cauliflower",
        inventory=25,
        price=19.99
    ),
    3: ItemModel(
        id=3,
        name="Moon Vaporizer",
        description="Vaporizes moons",
        inventory=2,
        price=5000.00
    )
}

# Get all items (GET request)
@router.get("/")
async def get_all_items():
    return item_database

# Subtract from item inventory (PATCH request)
# This function only updates inventory, so it should be a PATCH request, not a PUT
@router.patch("/{item_id}/subtract_inventory/{amount}")
async def subtract_from_inventory(item_id:int, amount:int):

    # Check if item exists

    # Make sure inventory won't be < 0

    # Subtract from inventory and return a message with the new inventory

    pass
