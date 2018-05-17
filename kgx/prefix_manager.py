import prefixcommons.curie_util as cu

class PrefixManager(object):
    """
    Manages prefix mappings.

    These include mappings for CURIEs such as GO:0008150, as well as shortforms such as
    biolink types such as Disease
    """
    def __init__(self, url=None):
        if url is None:
            url = "https://raw.githubusercontent.com/biolink/biolink-model/master/context.jsonld"

        # NOTE: this is cached
        # to clear cache: rm ~/.cachier/.prefixcommons.curie_util.read_remote_jsonld_context 
        self.set_prefixmap(cu.read_remote_jsonld_context(url))

    def set_prefixmap(self, m):
        self.prefixmap = m
        rm = {y: x for x, y in m.items() if isinstance(y, str)}
        self.rprefixmap = rm

    def expand(self, id):
        if id in self.prefixmap:
            return self.prefixmap[id]
        uri = cu.expand_uri(id, [self.prefixmap])
        return uri

    def contract(self, uri):
        # always prioritize non-CURIE shortform
        if uri in self.rprefixmap:
            return self.rprefixmap[uri]
        shortform = cu.contract_uri(uri, [self.prefixmap])
        if shortform == []:
            return None
        return shortform[0]
