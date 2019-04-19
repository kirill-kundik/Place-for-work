class CategoryRouter:

    async def index(self, request):
        pass

    async def one_category(self, request):
        pass

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/category', self.index, name='category')
        router.add_route('GET', '/category/{id}', self.one_category, name='one_category')
