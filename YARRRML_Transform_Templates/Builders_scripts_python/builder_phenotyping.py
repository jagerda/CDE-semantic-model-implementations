from embuilder.builder import EMB

prefixes = dict(
  rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#" ,
  rdfs = "http://www.w3.org/2000/01/rdf-schema#" ,
  obo = "http://purl.obolibrary.org/obo/" ,
  sio = "http://semanticscience.org/resource/" ,
  xsd = "http://www.w3.org/2001/XMLSchema#",
  this = "http://my_example.com/")


triplets = [

# Nodes
["this:$(pid)_$(uniqid)#ID","sio:SIO_000020","this:$(pid)_$(uniqid)#Phenotypic_Role","iri"],
["this:$(pid)_$(uniqid)#Entity","sio:SIO_000228","this:$(pid)_$(uniqid)#Phenotypic_Role","iri"],
["this:$(pid)_$(uniqid)#Entity","sio:SIO_000008","this:$(pid)_$(uniqid)#Phenotypic_Attribute","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Role","sio:SIO_000356","this:$(pid)_$(uniqid)#Phenotypic_Process","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Process","sio:SIO_000680","this:$(pid)_$(uniqid)#Phenotypic_Startdate","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Process","sio:SIO_000681","this:$(pid)_$(uniqid)#Phenotypic_Enddate","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Process","sio:SIO_000229","this:$(pid)_$(uniqid)#Phenotypic_Output","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Output","sio:SIO_000628","this:$(pid)_$(uniqid)#Phenotypic_Attribute","iri"],
# Types
["this:$(pid)_$(uniqid)#ID","rdf:type","sio:SIO_000115","iri"],
["this:$(pid)_$(uniqid)#Entity","rdf:type","sio:SIO_000498","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Role","rdf:type","sio:SIO_000016","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Role","rdf:type","obo:OBI_0000093","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Process","rdf:type","sio:SIO_000006","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Process","rdf:type","obo:OBI_0001546","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Process","rdf:type","obo:NCIT_C16205","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Process","rdf:type","obo:NCIT_C18020","iri"],

["this:$(pid)_$(uniqid)#Phenotypic_Startdate","rdf:type","sio:SIO_000031","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Enddate","rdf:type","sio:SIO_000032","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Output","rdf:type","sio:SIO_000015","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Output","rdf:type","obo:NCIT_C102741","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Attribute","rdf:type","sio:SIO_000614","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Attribute","rdf:type","sio:SIO_010056","iri"],
["this:$(pid)_$(uniqid)#Phenotypic_Attribute","rdf:type","$(HP_IRI)","iri"],

# Labels
["this:$(pid)_$(uniqid)#Phenotypic_Role","rdfs:label","Role: Phenotyping patient","xsd:string"],
["this:$(pid)_$(uniqid)#Phenotypic_Process","rdfs:label","Process: Comparative phenotypic assessment","xsd:string"],
["this:$(pid)_$(uniqid)#Phenotypic_Startdate","rdfs:label","Startdate: $(date)","xsd:string"],
["this:$(pid)_$(uniqid)#Phenotypic_Enddate","rdfs:label","Enddate: $(date)","xsd:string"],
["this:$(pid)_$(uniqid)#Phenotypic_Output","rdfs:label","Output type: $(HP_Label)","xsd:string"],
["this:$(pid)_$(uniqid)#Phenotypic_Attribute","rdfs:label","Attribute type: $(HP_Label)","xsd:string"],

# Values
["this:$(pid)_$(uniqid)#ID","sio:SIO_000300","$(pid)","xsd:string"],
["this:$(pid)_$(uniqid)#Phenotypic_Startdate","sio:SIO_000300","$(date)","xsd:date"],
["this:$(pid)_$(uniqid)#Phenotypic_Enddate","sio:SIO_000300","$(date)","xsd:date"]]

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