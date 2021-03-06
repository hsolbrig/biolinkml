# Auto generated from issue_260b.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-10-01 22:58
# Schema: issue_260b
#
# id: http://example.org/tests/issue_260b
# description: Another small file to be imported
# license:

import dataclasses
import sys
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from issue_260a import C260a, String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DEFAULT_ = CurieNamespace('', 'http://example.org/tests/issue_260b/')


# Types

# Class references



class C260b(C260a):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/issue_260b/C260b")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "C260b"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/issue_260b/C260b")



# Slots
class slots:
    pass

