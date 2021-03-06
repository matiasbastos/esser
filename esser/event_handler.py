import re
from esser.exceptions import AggregateDeleted

re_camel_case = re.compile(
    r'(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))'
)


def camel_case_to_spaces(value):
    """
    Splits CamelCase and converts to lower case. Also strips leading and
    trailing whitespace.
    """
    return re_camel_case.sub(r'_\1', value).strip('_').lower()


class BaseEventHandler(object):
    """
    Responsible for building up the read state from all events
    """

    def apply(self, aggregate, next_event):
        """Called by reduce(), this method should find the
        corresponding handler based on the event name

        Args:
            aggregate (dict): current state of an aggregate
            next_event (esser.repositories.base.Event): next event to apply

        Returns:
            dict: aggregate state
        """
        event_name = camel_case_to_spaces(next_event.event_type)
        self.update_version(aggregate, next_event)
        handler = getattr(self, 'on_%s' % event_name, None)
        if handler:
            return handler(aggregate, next_event)
        return aggregate

    def update_version(self, aggregate, next_event):
        aggregate['latest_version'] = next_event.version
        return aggregate

    def on_created(self, aggregate, next_event):
        aggregate.update(next_event.event_data)
        return aggregate

    def on_updated(self, aggregate, next_event):
        aggregate.update(next_event.event_data)
        return aggregate

    def on_deleted(self, aggregate, next_event):
        raise AggregateDeleted()

    def on_attribute_deleted(self, aggregate, next_event):
        for attr in next_event.event_data.get('attributes', []):
            aggregate.pop(attr, None)
        return aggregate
