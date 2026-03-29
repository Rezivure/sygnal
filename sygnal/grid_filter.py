# Grid-specific notification filtering for Sygnal.
# Drops events that should never generate a push notification.

import logging

logger = logging.getLogger(__name__)

# Event types to drop entirely (no push sent)
DROPPED_EVENT_TYPES = {
    "m.room.encryption",
    "m.room.power_levels",
    "m.room.name",
    "m.room.avatar",
    "m.room.topic",
    "m.room.canonical_alias",
    "m.room.join_rules",
    "m.room.history_visibility",
    "m.room.guest_access",
    "m.reaction",
    "m.room.redaction",
}


def should_send_push(notif):
    """
    Returns True if this notification should be dispatched to devices.
    Returns False to silently drop it (no push sent, no rejection reported).
    """
    if notif.type in DROPPED_EVENT_TYPES:
        logger.info(
            "Dropping push for event type %s in room %s",
            notif.type,
            notif.room_id,
        )
        return False

    return True
