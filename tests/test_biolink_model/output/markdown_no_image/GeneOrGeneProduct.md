
# Type: gene or gene product


a union of genes or gene products. Frequently an identifier for one will be used as proxy for another

URI: [biolink:GeneOrGeneProduct](https://w3id.org/biolink/vocab/GeneOrGeneProduct)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Transcript],[PhenotypicFeature],[OrganismTaxon],[NamedThing],[MolecularEntity],[MacromolecularMachine],[GenomicEntity],[GeneToThingAssociation],[GeneToPhenotypicFeatureAssociation],[GeneToGeneAssociation],[GeneToExpressionSiteAssociation],[GeneToDiseaseAssociation],[GeneRegulatoryRelationship],[GeneProduct],[OrganismTaxon]<in%20taxon(i)%200..*-%20[GeneOrGeneProduct&#124;name(i):symbol_type;has_biological_sequence(i):biological_sequence%20%3F;id(i):identifier_type;category(i):iri_type%20%2B],[ChemicalToGeneAssociation]-%20object%201..1>[GeneOrGeneProduct],[GeneAsAModelOfDiseaseAssociation]-%20subject%201..1>[GeneOrGeneProduct],[GeneHasVariantThatContributesToDiseaseAssociation]-%20subject%201..1>[GeneOrGeneProduct],[GeneRegulatoryRelationship]-%20object%201..1>[GeneOrGeneProduct],[GeneRegulatoryRelationship]-%20subject%201..1>[GeneOrGeneProduct],[GeneToDiseaseAssociation]-%20subject%201..1>[GeneOrGeneProduct],[GeneToExpressionSiteAssociation]-%20subject%201..1>[GeneOrGeneProduct],[GeneToGeneAssociation]-%20object%201..1>[GeneOrGeneProduct],[GeneToGeneAssociation]-%20subject%201..1>[GeneOrGeneProduct],[GeneToPhenotypicFeatureAssociation]-%20subject%201..1>[GeneOrGeneProduct],[GeneToThingAssociation]-%20subject%201..1>[GeneOrGeneProduct],[GeneOrGeneProduct]^-[GeneProduct],[GeneOrGeneProduct]^-[Gene],[MacromolecularMachine]^-[GeneOrGeneProduct],[GeneHasVariantThatContributesToDiseaseAssociation],[GeneAsAModelOfDiseaseAssociation],[Gene],[DiseaseOrPhenotypicFeature],[ChemicalToGeneAssociation],[AnatomicalEntity])

## Parents

 *  is_a: [MacromolecularMachine](MacromolecularMachine.md) - A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.

## Children

 * [Gene](Gene.md)
 * [GeneProduct](GeneProduct.md) - The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules

## Referenced by class

 *  **[ChemicalToGeneAssociation](ChemicalToGeneAssociation.md)** *[chemical to gene association➞object](chemical_to_gene_association_object.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[AnatomicalEntity](AnatomicalEntity.md)** *[expresses](expresses.md)*  <sub>0..*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md)** *[gene as a model of disease association➞subject](gene_as_a_model_of_disease_association_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md)** *[gene has variant that contributes to disease association➞subject](gene_has_variant_that_contributes_to_disease_association_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneRegulatoryRelationship](GeneRegulatoryRelationship.md)** *[gene regulatory relationship➞object](gene_regulatory_relationship_object.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneRegulatoryRelationship](GeneRegulatoryRelationship.md)** *[gene regulatory relationship➞subject](gene_regulatory_relationship_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)** *[gene to disease association➞subject](gene_to_disease_association_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[gene to expression site association➞subject](gene_to_expression_site_association_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToGeneAssociation](GeneToGeneAssociation.md)** *[gene to gene association➞object](gene_to_gene_association_object.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToGeneAssociation](GeneToGeneAssociation.md)** *[gene to gene association➞subject](gene_to_gene_association_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md)** *[gene to phenotypic feature association➞subject](gene_to_phenotypic_feature_association_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToThingAssociation](GeneToThingAssociation.md)** *[gene to thing association➞subject](gene_to_thing_association_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[in cell population with](in_cell_population_with.md)*  <sub>0..*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[in complex with](in_complex_with.md)*  <sub>0..*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[in pathway with](in_pathway_with.md)*  <sub>0..*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**

## Attributes


### Inherited from genomic entity:

 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)
    * inherited from: [NamedThing](NamedThing.md)

### Inherited from macromolecular machine:

 * [macromolecular machine➞name](macromolecular_machine_name.md)  <sub>REQ</sub>
    * range: [SymbolType](types/SymbolType.md)
    * inherited from: [MacromolecularMachine](MacromolecularMachine.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](types/IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [expressed in](expressed_in.md)  <sub>0..*</sub>
    * Description: holds between a gene or gene product and an anatomical entity in which it is expressed
    * range: [AnatomicalEntity](AnatomicalEntity.md)
    * in subsets: (translator_minimal)
 * [in cell population with](in_cell_population_with.md)  <sub>0..*</sub>
    * Description: holds between two genes or gene products that are expressed in the same cell type or population
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * in subsets: (translator_minimal)
 * [in complex with](in_complex_with.md)  <sub>0..*</sub>
    * Description: holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * in subsets: (translator_minimal)
 * [in pathway with](in_pathway_with.md)  <sub>0..*</sub>
    * Description: holds between two genes or gene products that are part of in the same biological pathway
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * in subsets: (translator_minimal)