# The upper domain model is generic across different data management domain applications. 
# Created 2019-07-12 16:49:32.398000 

# Dict storing class info: 
classes = [{'KBMSThing': {'admin': 'yes',
                'description': 'Mother of all knowledge instances',
                'html_info': 'Add a new general item that does not have a specific type.',
                'identifier': 'http://example.org/tbox/kbmsthing',
                'label': 'TBox',
                'ontology_level': 'upper',
                'optional_property': [],
                'pl': 'KBMS Things',
                'required_property': ['description', 'identifier', 'title'],
                'sing': 'KBMS Thing',
                'subclass_of': 'NULL',
                'title': 'KBMSThing',
                'version': 'v3.1'}},
 {'Agent': {'admin': 'yes',
            'description': 'Things or people that can create knowledge, like users, organization, or systems',
            'html_info': '',
            'identifier': 'http://example.org/tbox/agent',
            'label': 'TBox',
            'ontology_level': 'upper',
            'optional_property': [],
            'pl': 'Agents',
            'required_property': [],
            'sing': 'Agent',
            'subclass_of': 'KBMSThing',
            'title': 'Agent',
            'version': 'v3.1'}},
 {'Activity': {'admin': '',
               'description': 'A frame for certain knowledge, like a project or a project phase',
               'html_info': '',
               'identifier': 'http://example.org/tbox/activity',
               'label': 'TBox',
               'ontology_level': 'upper',
               'optional_property': [],
               'pl': 'Activities',
               'required_property': [],
               'sing': 'Activity',
               'subclass_of': 'KBMSThing',
               'title': 'Activity',
               'version': 'v3.1'}},
 {'Data': {'admin': '',
           'description': 'A digital representation of knowledge',
           'html_info': '',
           'identifier': 'http://example.org/tbox/data',
           'label': 'TBox',
           'ontology_level': 'upper',
           'optional_property': ['subject'],
           'pl': 'Data',
           'required_property': [],
           'sing': 'Data',
           'subclass_of': 'KBMSThing',
           'title': 'Data',
           'version': 'v3.1'}}]

# Dict storing relation info. 
relations = [{'references': {'description': 'A related KBMSThing  that is referenced, cited, or otherwise pointed to by the described KBMSThing',
                 'from_entity': 'KBMSThing',
                 'identifier': 'http://example.org/tbox/references',
                 'label': 'object_property',
                 'level': 'upper',
                 'namespace': 'dcterms',
                 'to_entity': 'KBMSThing'}},
 {'relation': {'description': 'A relation between two KBMSThings (bi-directional version of references)',
               'from_entity': 'KBMSThing',
               'identifier': 'http://example.org/tbox/relation',
               'label': 'object_property',
               'level': 'upper',
               'namespace': 'dcterms',
               'to_entity': 'KBMSThing'}},
 {'haspart': {'description': 'A related KBMSThing that is included either physically or logically in the described KBMSThing.',
              'from_entity': 'KBMSThing',
              'identifier': 'http://example.org/tbox/haspart',
              'label': 'object_property',
              'level': 'upper',
              'namespace': 'dcterms',
              'to_entity': 'KBMSThing'}},
 {'rights': {'description': 'The Document includes  a statement about various property rights associated with the KBMSThing, including intellectual property rights.',
             'from_entity': 'KBMSThing',
             'identifier': 'http://example.org/tbox/rights',
             'label': 'object_property',
             'level': 'upper',
             'namespace': 'dcterms',
             'to_entity': 'Document'}},
 {'rightsholder': {'description': 'A person or organization owning or managing rights over the KBMSThing',
                   'from_entity': 'KBMSThing',
                   'identifier': 'http://example.org/tbox/rightsholder',
                   'label': 'object_property',
                   'level': 'upper',
                   'namespace': 'dcterms',
                   'to_entity': 'Agent'}}]

# Dict storing property info. 
properties = [
 {'title': {'description': 'A name given to the KBMSThing',
            'identifier': 'http://example.org/tbox/title',
            'label': 'property',
            'label2': 'TBox',
            'namespace': 'dcterms',
            'title': 'title',
            'unique': 'False',
            'xsd_type': 'xsd:string'}},
 {'description': {'description': 'tbd',
                  'identifier': 'http://example.org/tbox/description',
                  'label': 'property',
                  'label2': 'TBox',
                  'namespace': 'dcterms',
                  'title': 'description',
                  'unique': 'False',
                  'xsd_type': 'xsd:string'}},
 {'identifier': {'description': 'A URI that uniquely identifies this thing',
                 'identifier': 'http://example.org/tbox/identifier',
                 'label': 'property',
                 'label2': 'TBox',
                 'namespace': 'dcterms',
                 'title': 'identifier',
                 'unique': 'True',
                 'xsd_type': 'xsd:anyURI'}}]

# Dict storing namespace info. 
namespaces = [{'dcterms': {'comment': '',
              'uri': 'http://purl.org/dc/terms/',
              'url': 'www.dublincore.org/documents/dcmi-terms/'}},
 {'rdfs': {'comment': '',
           'uri': '',
           'url': 'https://www.w3.org/TR/2014/REC-rdf-schema-20140225/'}},
 {'kb': {'comment': 'upper / generic terms for knowledge management system',
         'uri': 'tdb: somewhere under MOBI?',
         'url': ''}},
 {'stkb': {'comment': 'lower / Simutool specific terms',
           'uri': 'tbd: somewhere under MOBI or under simutool.com?',
           'url': ''}},
 {'foaf': {'comment': '', 'uri': '', 'url': 'http://xmlns.com/foaf/spec/'}}]
