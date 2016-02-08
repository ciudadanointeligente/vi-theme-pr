from elections.views import SoulMateDetailView


class MediaNaranjaView(SoulMateDetailView):
    def get_information_holder(self, data={}):
        holder = super(MediaNarajaView, self).get_information_holder(data)
        return holder
