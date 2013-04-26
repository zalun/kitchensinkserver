"""
base.models
-----------
"""
from django.core.urlresolvers import reverse
from django.db import models, IntegrityError


class BaseModel(models.Model):
    """Force validation and privileges tests before save

    Call ``default_{field_name}`` methods which are setting the default value
    of the field when creating a new instance. `(Original Source)
    <https://github.com/seanmonstar/FlightDeck/blob/apps/base/models.py>`_

    Provide methods to get API urls.

    :Authors:

       * Created by Sean McArthur for Mozilla Addons Builder,
       * Modified by Piotr Zalewa for KitchensinkServer
    """
    resource_name = None

    class Meta:
        #:
        abstract = True

    def __init__(self, *args, **kwargs):
        """Implements ``creating`` attribute to ``_state`` object to provide
        more accurate information than original ``adding``.
        """
        super(BaseModel, self).__init__(*args, **kwargs)
        self.set_state()

    def set_state(self, force_insert=False):
        self._state.creating = False if self.pk and not force_insert else True

    def save(self, **kwargs):
        """Implements ``creating`` attribute to ``_state`` field to provide
        more accurate information than original ``adding``.

        If creating a new instance call all ``default_{field_name}`` methods
        (which are defined in a subclass) to set default values.

        Call all ``update_{field_name}`` methads (which are defined in
        subclass) to set update values for every save.

        Validate model for every save by calling ``full_clean`` and
        ``check_privileges`` methods.
        """
        self.set_state(force_insert=kwargs.get('force_insert', False))
        if self._state.creating:
            for attrName in dir(self):
                if attrName.find('default_') != 0:
                    continue
                attr = getattr(self, attrName)
                if callable(attr):
                    field = attrName[8:]
                    try:
                        orig = getattr(self, field)
                    except:
                        # this method is working for fields not exposed
                        # in class definition
                        orig = None
                    if orig is None or orig == '':
                        attr()

        for attrName in dir(self):
            if attrName.find('update_') != 0:
                continue
            attr = getattr(self, attrName)
            if callable(attr):
                attr()

        self.full_clean()
        self.check_privileges(**kwargs)
        return super(BaseModel, self).save(**kwargs)

    def check_privileges(self, **kwargs):
        """ A placeholder for a method which should be overriden to check for
        privileges
        """
        pass

    def get_resource_uri(self, api_name):
        if not self.resource_name:
            return
        return reverse('api_dispatch_detail', kwargs={'api_name': api_name,
            'resource_name': self.resource_name, 'pk': self.pk})

    @classmethod
    def get_api_uri(cls, api_name):
        if not cls.resource_name:
            return
        return reverse('api_dispatch_list', kwargs={'api_name': api_name,
            'resource_name': cls.resource_name})

