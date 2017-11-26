
def prevent_search(relation):
    """
    Used to mark a model field or relation as "restricted from filtering"
    e.g.,

    class AuthToken(BaseModel):
        user = prevent_search(models.ForeignKey(...))
        sensitive_data = prevent_search(models.CharField(...))

    The flag set by this function is used by
    `awx.api.filters.FieldLookupBackend` to blacklist fields and relations that
    should not be searchable/filterable via search query params
    """
    setattr(relation, '__prevent_search__', True)
    return relation