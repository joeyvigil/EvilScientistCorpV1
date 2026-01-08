from typing import Annotated, Optional

from pydantic import BaseModel, Field

# Check user_model for relevant notes

class ItemModel(BaseModel):
    # Optional - another way to make this value optional
    # like setting "= None" like we did in UserModel
    id: Optional[int, Field(gt=0)]
    name: Annotated[str, Field(min_length=3, max_length=50)]
    description: Annotated[str, Field(min_length=10, max_length=100)]
    # ge = greater than or equal to
    # lt = less than or equal to
    inventory: Annotated[int, Field(ge=0, le=100)]
    price: Annotated[float, Field(gt=0)]