"""Module containing functions for using the snippet service end-point
"""

from lm_client.common.api_service import RestService

# .............................................................................
class SnippetApiService(RestService):
    """This class is used for working with the snippet service end-point
    """
    end_point = 'api/v2/snippet/'

    # ...........................
    def list(self, raw=False, after_time=None, agent=None, before_time=None,
             catalog_number=None, collection=None, ident1=None, ident2=None,
             operation=None, provider=None, url=None, who=None, why=None):
        """Lists snippets matching the provided criteria.

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object.  If False, load into JSON.
            after_time (:obj:`str`, optional): Only return snippets modified
                after this time (in ISO-8601 format).
            agent (:obj:`str`, optional): Return snippets initiated by this
                agent.
            before_time (:obj:`str`, optional): Only return snippets modified
                before this time (in ISO-8601 format).
            catalog_number (:obj:`str`, optional): List snippets for occurrence
                records with this catalog number.
            collection (:obj:`str`, optional): List snippets for this
                collection.
            ident1 (:obj:`str`, optional): List snippets with this primary
                object identifier.
            ident2 (:obj:`str`, optional): List snippets with this secondary
                object identifier.
            operation (:obj:`str`, optional): List snippets for this operation.
            provider (:obj:`str`, optional): List snippets for this occurrence
                point provider.
            url (:obj:`str`, optional): List snippets related to this URL.
            who (:obj:`str`, optional): List snippets created by this entity.
            why (:obj:`str`, optional): List snippets that were created for
                this reason.
        """
        return RestService.list(self,
            self.end_point, raw=raw, after_time=after_time, agent=agent,
            before_time=before_time, catalog_number=catalog_number,
            collection=collection, ident1=ident1, ident2=ident2,
            operation=operation, provider=provider, url=url, who=who, why=why)
