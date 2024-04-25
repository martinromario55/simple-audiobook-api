from fastapi import APIRouter, status, HTTPException

from api.data import parse_json_data




router = APIRouter(
    prefix="/api/v1/audiobooks",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)


# Get All Audiobooks
@router.get("/", status_code=status.HTTP_200_OK)
def read_root():
    try:
        audiobooks = parse_json_data("./api/audiobooks.json")
        return {"audiobooks": audiobooks}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    
# Get One Audiobook
@router.get("/{id}", status_code=status.HTTP_200_OK)
def read_audiobook(id: int):
    try:
        data = parse_json_data("./api/audiobooks.json")
        # loop through the data
        for audiobook in data:
            if audiobook["id"] == id:
                return {"audiobook": audiobook}
            
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Audiobook with id {id} was not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
# Search Audiobook using Title or author's name

