from django.db import models


class CRAWLING_STATUSES:
    NOT_CRAWLED = 0
    ERROR_REQUESTING_LINK = 1
    UPDATING_LINK = 2
    MARKED_AS_DUPLICATE = 3
    UPDATED_LINK = 4
    CRAWLING = 5
    CRAWLING_FAILED = 6
    RESCHEDULED_LONG_CRAWLING = 7
    CRAWLING_TOO_LONG = 8
    HAS_NO_PAGES = 9
    TEXT_UPLOADED = 10
    AWAITING_CRAWL = 11
    INDEXED_BY_ELASTIC = 12
    TEXT_ANALYZED = 13
    DOMAIN_INVALID = 14
    NO_LINKS_IN_PAGE = 15
    UNCRAWLABLE = 16


# Create your models here.
class NotificationModel(models.Model):
    
    class Meta:
        abstract = True
        
    def save(self, *args, **kwargs):
        print("notify on", self.__str__)
        super().save(*args, **kwargs)


class CrawlableEntity(NotificationModel):
    link: models.TextField()
    name: models.TextField()
    crawling_status: models.IntegerField(default = CRAWLING_STATUSES.NOT_CRAWLED)
    is_deleted: models.BooleanField(default=False)
    is_blacklisted: models.BooleanField(default=False)
    last_crawled: models.DateField(null=True)

