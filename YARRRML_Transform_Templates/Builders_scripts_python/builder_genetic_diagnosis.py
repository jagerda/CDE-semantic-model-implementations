from embuilder.builder import EMB

prefixes = dict(
  rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#" ,
  rdfs = "http://www.w3.org/2000/01/rdf-schema#" ,
  obo = "http://purl.obolibrary.org/obo/" ,
  sio = "http://semanticscience.org/resource/" ,
  xsd = "http://www.w3.org/2001/XMLSchema#",
  edam = "http://edamontology.org/",
  this = "http://my_example.com/")


triplets = [

# Nodes
["this:$(pid)_$(uniqid)#ID","sio:SIO_000020","this:$(pid)_$(uniqid)#Genetic_Role","iri"],
["this:$(pid)_$(uniqid)#Entity","sio:SIO_000228","this:$(pid)_$(uniqid)#Genetic_Role","iri"],
["this:$(pid)_$(uniqid)#Entity","sio:SIO_000008","this:$(pid)_$(uniqid)#HGVS_Attribute","iri"],
["this:$(pid)_$(uniqid)#Entity","sio:SIO_000008","$(omim_uri)","iri"],
["this:$(pid)_$(uniqid)#Entity","sio:SIO_000008","$(clinvar_uri)","iri"],

["this:$(pid)_$(uniqid)#Genetic_Role","sio:SIO_000356","this:$(pid)_$(uniqid)#HGVS_Process","iri"],
["this:$(pid)_$(uniqid)#Genetic_Role","sio:SIO_000356","this:$(pid)_$(uniqid)#OMIM_Process","iri"],
["this:$(pid)_$(uniqid)#Genetic_Role","sio:SIO_000356","this:$(pid)_$(uniqid)#HGNC_Process","iri"],

["this:$(pid)_$(uniqid)#HGVS_Process","sio:SIO_000229","this:$(pid)_$(uniqid)#HGVS_Output","iri"],
["this:$(pid)_$(uniqid)#HGVS_Output","sio:SIO_000628","this:$(pid)_$(uniqid)#HGVS_Attribute","iri"],

["this:$(pid)_$(uniqid)#OMIM_Process","sio:SIO_000229","this:$(pid)_$(uniqid)#OMIM_Output","iri"],
["this:$(pid)_$(uniqid)#OMIM_Output","sio:SIO_000628","$(omim_uri)","iri"],

["this:$(pid)_$(uniqid)#HGNC_Process","sio:SIO_000229","this:$(pid)_$(uniqid)#HGNC_Output","iri"],
["this:$(pid)_$(uniqid)#HGNC_Output","sio:SIO_000628","$(clinvar_uri)","iri"],

# Types
["this:$(pid)_$(uniqid)#ID","rdf:type","sio:SIO_000115","iri"],
["this:$(pid)_$(uniqid)#Entity","rdf:type","sio:SIO_000498","iri"],
["this:$(pid)_$(uniqid)#Genetic_Role","rdf:type","sio:SIO_000016","iri"],
["this:$(pid)_$(uniqid)#Genetic_Role","rdf:type","obo:OBI_0000093","iri"],

["this:$(pid)_$(uniqid)#HGVS_Process","rdf:type","obo:NCIT_C15709","iri"],
["this:$(pid)_$(uniqid)#HGVS_Process","rdf:type","sio:SIO_000006","iri"],
["this:$(pid)_$(uniqid)#HGVS_Output","rdf:type","sio:SIO_000015","iri"],
["this:$(pid)_$(uniqid)#HGVS_Output","rdf:type","sio:SIO_001388","iri"],
["this:$(pid)_$(uniqid)#HGVS_Attribute","rdf:type","sio:SIO_000614","iri"],
["this:$(pid)_$(uniqid)#HGVS_Attribute","rdf:type","sio:SIO_000015","iri"],
["this:$(pid)_$(uniqid)#HGVS_Attribute","rdf:type","obo:NCIT_C171178","iri"],

["this:$(pid)_$(uniqid)#OMIM_Process","rdf:type","obo:NCIT_C15709","iri"],
["this:$(pid)_$(uniqid)#OMIM_Process","rdf:type","sio:SIO_000006","iri"],
["this:$(pid)_$(uniqid)#OMIM_Output","rdf:type","sio:SIO_000015","iri"],
["this:$(pid)_$(uniqid)#OMIM_Output","rdf:type","sio:SIO_001381","iri"],
["$(omim_uri)","rdf:type","sio:SIO_000614","iri"],
["$(omim_uri)","rdf:type","sio:SIO_000015","iri"],
["$(omim_uri)","rdf:type","edam:data_1153","iri"],

["this:$(pid)_$(uniqid)#HGNC_Process","rdf:type","obo:NCIT_C15709","iri"],
["this:$(pid)_$(uniqid)#HGNC_Process","rdf:type","sio:SIO_000006","iri"],
["this:$(pid)_$(uniqid)#HGNC_Output","rdf:type","sio:SIO_000015","iri"],
["this:$(pid)_$(uniqid)#HGNC_Output","rdf:type","sio:SIO_001381","iri"],
["$(clinvar_uri)","rdf:type","sio:SIO_000614","iri"],
["$(clinvar_uri)","rdf:type","sio:SIO_000015","iri"],
["$(clinvar_uri)","rdf:type","edam:data_2298","iri"],


# Labels
["this:$(pid)_$(uniqid)#Genetic_Role","rdfs:label","Role: Genetic diagnosis patient","xsd:string"],
["this:$(pid)_$(uniqid)#HGVS_Process","rdfs:label","Process: HGVS genetic testing","xsd:string"],
["this:$(pid)_$(uniqid)#HGVS_Output","rdfs:label","Output type: HGVS measurement value","xsd:string"],
["this:$(pid)_$(uniqid)#HGVS_Attribute","rdfs:label","Attribute type: $(hgvs_string)","xsd:string"],

["this:$(pid)_$(uniqid)#OMIM_Process","rdfs:label","Process: OMIM genetic testing","xsd:string"],
["this:$(pid)_$(uniqid)#OMIM_Output","rdfs:label","Output type: OMIM genome sequence variant","xsd:string"],
["$(omim_uri)","rdfs:label","Attribute type: $(omim_uri)","xsd:string"],

["this:$(pid)_$(uniqid)#HGNC_Process","rdfs:label","Process: HGNC genetic testing","xsd:string"],
["this:$(pid)_$(uniqid)#HGNC_Output","rdfs:label","Output type: HGNC genome sequence variant","xsd:string"],
["$(clinvar_uri)","rdfs:label","Attribute type: $(clinvar_uri)","xsd:string"],

# Values
["this:$(pid)_$(uniqid)#ID","sio:SIO_000300","$(pid)","xsd:string"],
["this:$(pid)_$(uniqid)#HGVS_Output","sio:SIO_000300","$(hgvs_string)","xsd:string"],
["this:$(pid)_$(uniqid)#OMIM_Output","sio:SIO_000300","$(omim_uri)","xsd:string"],
["this:$(pid)_$(uniqid)#HGNC_Output","sio:SIO_000300","$(clinvar_uri)","xsd:string"]]


config = dict(
  source_name = "source_cde_test",
  configuration = "ejp",    # Two options for this parameter:
                            # ejp: it defines CDE-in-a-Box references, being compatible with this workflow  
                            # csv: No workflow defined, set the source configuration for been used by CSV as data source
                            
  csv_name = "source_1" # parameter only needed in case you pick "csv" as configuration
)

yarrrml = EMB(config)
test = yarrrml.transform(prefixes, triplets)
print(test)