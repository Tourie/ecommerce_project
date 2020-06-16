from django.urls import reverse, resolve


class TestShopsUrls:

    def test_shop_detail_url(self):
        path = reverse('shop_detail_url', kwargs={'title': 'amazon'})
        assert resolve(path).view_name == 'shop_detail_url'

    def test_shop_list_url(self):
        path = reverse('shops_list_url')
        assert resolve(path).view_name == 'shops_list_url'

    def test_item_detail_url(self):
        path = reverse('item_detail_url', kwargs={'title': 'title'})
        assert resolve(path).view_name == "item_detail_url"
