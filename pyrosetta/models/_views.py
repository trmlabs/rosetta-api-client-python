import inspect
from typing import Type

from json2html import json2html
from pydantic import BaseModel
import yaml

from . import _models as m

def _str(self : Type[BaseModel]) -> str:
    return yaml.dump(self.dict(), default_flow_style=False)

def _repr_html_(self : Type[BaseModel]) -> str:
    return json2html.convert(json=self.json())

for name, model in inspect.getmembers(m, inspect.isclass(m)):
    try:
        if issubclass(model, BaseModel):
            model.__str__ = _str
            model._repr_html_ = _repr_html_
    except TypeError:
        pass