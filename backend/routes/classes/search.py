class SearchRoute:

    async def search(self, request):
        pass

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/search', self.search, name='search')
