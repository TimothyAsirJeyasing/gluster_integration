from tendrl.commons import objects


class GlobalDetails(objects.BaseObject):
    def __init__(self, status=None, connection_count=0,
                 connection_active=0, volume_up_degraded=0,
                 peer_count=0, vol_count=0,
                 *args, **kwargs):
        super(GlobalDetails, self).__init__(*args, **kwargs)

        self.status = status
        self.connection_count = connection_count
        self.connection_active = connection_active
        self.volume_up_degraded = volume_up_degraded
        self.peer_count = peer_count
        self.vol_count = vol_count
        self.value = 'clusters/{0}/GlobalDetails'

    def render(self):
        self.value = self.value.format(NS.tendrl_context.integration_id)
        return super(GlobalDetails, self).render()
