from typing import List
from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader, TextLoader

class DocumentLoader:
    def __init__(self, docs_folder: str):
        self.docs_folder = docs_folder

    def _load_pdf(self) -> List:
        """Load PDF files from the documents folder."""
        loader = DirectoryLoader(self.docs_folder, glob="**/*.pdf", loader_cls=PyMuPDFLoader)
        return loader.load()

    def _load_txt(self) -> List:
        """Load TXT files from the documents folder."""
        loader = DirectoryLoader(self.docs_folder, glob="**/*.txt", loader_cls=TextLoader)
        return loader.load()

    def load_documents(self) -> List:
        """Load all supported document types."""
        docs = self._load_pdf()
        docs.extend(self._load_txt())
        print(f"Total documents loaded: {len(docs)}")
        return docs