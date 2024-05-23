import re
from . import node


class IDLAnnotation(node.IDLNode):
    def __init__(self, annotation, parent):
        super(IDLAnnotation, self).__init__('IDLAnnotation', annotation, parent)
        self._annotation = re.sub(r'^.*?//@', '', annotation).strip()

    @property
    def annotation(self):
        return self._annotation
