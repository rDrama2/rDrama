import time
from os import environ

from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *

from files.classes import Base
from files.helpers.lazy import lazy
from files.helpers.const import *

from .sub_relationship import *

class Sub(Base):
	__tablename__ = "subs"
	name = Column(String, primary_key=True)
	sidebar = Column(String)
	sidebar_html = Column(String)
	sidebarurl = Column(String)
	bannerurl = Column(String)
	marseyurl = Column(String)
	css = Column(String)
	stealth = Column(Boolean)
	created_utc = Column(Integer)

	blocks = relationship("SubBlock", primaryjoin="SubBlock.sub==Sub.name")
	followers = relationship("SubSubscription", primaryjoin="SubSubscription.sub==Sub.name")
	joins = relationship("SubJoin", lazy="dynamic", primaryjoin="SubJoin.sub==Sub.name")

	def __init__(self, *args, **kwargs):
		if "created_utc" not in kwargs: kwargs["created_utc"] = int(time.time())
		super().__init__(*args, **kwargs)

	def __repr__(self):
		return self.name

	@property
	@lazy
	def sidebar_url(self):
		if self.sidebarurl: return SITE_FULL + self.sidebarurl
		return f'/i/{SITE_NAME}/sidebar.webp?v=3009'

	@property
	@lazy
	def banner_url(self):
		if self.bannerurl: return SITE_FULL + self.bannerurl
		return f'/i/{SITE_NAME}/banner.webp?v=3009'

	@property
	@lazy
	def marsey_url(self):
		if self.marseyurl: return SITE_FULL + self.marseyurl
		return f'/i/{SITE_NAME}/headericon.webp?v=3009'

	@property
	@lazy
	def join_num(self):
		return self.joins.count()

	@property
	@lazy
	def block_num(self):
		return len(self.blocks)

	@property
	@lazy
	def follow_num(self):
		return len(self.followers)
