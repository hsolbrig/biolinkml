
# Type: thing with taxon


A mixin that can be used on any entity with a taxon

URI: [biolink:ThingWithTaxon](https://w3id.org/biolink/vocab/ThingWithTaxon)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon]<in%20taxon%200..*-%20[ThingWithTaxon],[PopulationOfIndividualOrganisms]uses%20-.->[ThingWithTaxon],[MolecularEntity]uses%20-.->[ThingWithTaxon],[LifeStage]uses%20-.->[ThingWithTaxon],[IndividualOrganism]uses%20-.->[ThingWithTaxon],[DiseaseOrPhenotypicFeature]uses%20-.->[ThingWithTaxon],[AnatomicalEntity]uses%20-.->[ThingWithTaxon],[PopulationOfIndividualOrganisms],[OrganismTaxon],[MolecularEntity],[LifeStage],[IndividualOrganism],[DiseaseOrPhenotypicFeature],[AnatomicalEntity])

## Mixin for

 * [AnatomicalEntity](AnatomicalEntity.md) (mixin)  - A subcellular location, cell type or gross anatomical part
 * [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) (mixin)  - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
 * [IndividualOrganism](IndividualOrganism.md) (mixin) 
 * [LifeStage](LifeStage.md) (mixin)  - A stage of development or growth of an organism, including post-natal adult stages
 * [MolecularEntity](MolecularEntity.md) (mixin)  - A gene, gene product, small molecule or macromolecule (including protein complex)
 * [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) (mixin)  - A collection of individuals from the same taxonomic class distinguished by one or more characteristics. Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance for Genome Resources]

## Referenced by class


## Attributes


### Own

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)
