from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chemdataextractor import Document

app = FastAPI(title="ChemGPT Extract Service")

class TextInput(BaseModel):
    text: str

@app.post("/extract")
def extract_chem_entities(input: TextInput):
    try:
        doc = Document(input.text)
        entities = {
            "compounds": [c.text for c in doc.cems]
            # "properties" extraction is removed; v2.x requires custom parsers.
        }
        return {"success": True, "entities": entities}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "ChemGPT Extract API is alive!"}
