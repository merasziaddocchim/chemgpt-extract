from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chemdataextractor import Document

# Create the FastAPI app with a descriptive title
app = FastAPI(title="ChemGPT Extract Service")

# Define the request body model for input text
class TextInput(BaseModel):
    text: str  # User will send {"text": "some text here"}

@app.post("/extract")
def extract_chem_entities(input: TextInput):
    """
    Extract chemical entity names from input text using ChemDataExtractor.
    Example input: {"text": "Aspirin and benzene are common."}
    Example output: {"success": True, "entities": {"compounds": ["aspirin", "benzene"]}}
    """
    try:
        # Parse the text and extract all chemical names/entities
        doc = Document(input.text)
        entities = {
            "compounds": [c.text for c in doc.cems]
            # Add more entity types here if needed (properties, etc.)
        }
        return {"success": True, "entities": entities}
    except Exception as e:
        # Catch any errors and return as HTTP 500 for debugging
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    """
    Health check endpoint for Railway/up monitoring.
    """
    return {"message": "ChemGPT Extract API is alive!"}
