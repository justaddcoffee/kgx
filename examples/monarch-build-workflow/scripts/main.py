"""
Loads all the turtle files with their required ontologies and transforms them to
json. Then loads all these json files, along with the semmeddb edges.csv and
nodes.csv files, into a single NetworkX graph, and performs `clique_merge` on it.
Finally, saves the resulting NetworkX graph as `clique_merged.csv`
"""

from kgx import ObanRdfTransformer2, JsonTransformer, HgncRdfTransformer, RdfOwlTransformer2
from kgx import clique_merge, make_valid_types

t = RdfOwlTransformer2()
t.parse('data/hp.owl')
t = JsonTransformer(t)
t.save('results/hp.json')

t = RdfOwlTransformer2()
t.parse('data/mondo.owl')
t = JsonTransformer(t)
t.save('results/mondo.json')

t = HgncRdfTransformer()
t.parse('data/hgnc.ttl')
t = JsonTransformer(t)
t.save('results/hgnc.json')

t = ObanRdfTransformer2()
t.add_ontology('data/mondo.owl')
t.add_ontology('data/hp.owl')
t.parse('data/orphanet.ttl')
t = JsonTransformer(t)
t.save('results/orphanet.json')

t = ObanRdfTransformer2()
t.add_ontology('data/mondo.owl')
t.add_ontology('data/hp.owl')
t.parse('data/hpoa.ttl')
t = JsonTransformer(t)
t.save('results/hpoa.json')

t = ObanRdfTransformer2()
t.add_ontology('data/mondo.owl')
t.parse('data/omim.ttl')
t = JsonTransformer(t)
t.save('results/omim.json')

t = ObanRdfTransformer2()
t.add_ontology('data/mondo.owl')
t.add_ontology('data/go.owl')
t.add_ontology('data/so.owl')
t.parse('data/clinvar.ttl')
t = JsonTransformer(t)
t.save('results/clinvar.json')

t = JsonTransformer()
t.parse('results/hp.owl')
t.parse('results/mondo.json')
t.parse('results/hgnc.json')
t.parse('results/clinvar.json')
t.parse('results/omim.json')
t.parse('results/hpoa.json')
t.parse('results/orphanet.json')

t = PandasTransformer(t.graph)
t.parse('data/semmeddb_edges.csv')
t.parse('data/semmeddb_nodes.csv')

t.graph = clique_merge(t.graph)
t.graph = make_valid_types(t.graph)

t.save('results/clique_merged.csv')
