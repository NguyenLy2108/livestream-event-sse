from livestream_status.route import router as LivestreamStatus

ROUTE_LIST = [
    {'route': LivestreamStatus, 'tags': ['Livestream Status'], 'prefix': '/stream'},
]