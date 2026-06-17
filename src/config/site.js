const SITE_URL = import.meta.env.PUBLIC_SITE_URL || 'http://localhost:5200';

export const siteConfig = {
	title: "Portfolio",
	author: "Designer",
	url: SITE_URL,
	mail: "hello@example.com",
	resume: "/images/resume/",
	utm: {
		source: `${SITE_URL}`,
		medium: "referral",
		campaign: "navigation",
	},
	meta:{
		title: "作品集 | Portfolio",
		description: "个人作品展示 — 包含直播画面设计、海报设计、抖音产品图、店铺装修、详情页等作品。",
		keywords: "作品集, 设计, 直播设计, 海报, 抖音, 电商设计",
		image: `${SITE_URL}/og.jpg`,
		twitterHandle: "",
	},
	social:{
		twitter: "",
		twitterName: "",
		github: "",
		blog: "",
		xiaohongshu: "",
		zcool: "",
		behance: "",
	},
};
