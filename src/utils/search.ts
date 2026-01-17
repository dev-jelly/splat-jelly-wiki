const searchIndex = [
  {
    title: "새먼 런 메인",
    url: "/",
    description: "스플래툰 3 새먼 런 NEXT WAVE의 전체 개요와 기본 정보"
  },
  {
    title: "스테이지 목록",
    url: "/stages/",
    description: "새먼 런의 모든 스테이지와 특징"
  },
  {
    title: "셰케나 댐",
    url: "/stages/spawning-grounds/",
    description: "새먼 런 스테이지 - Spawning Grounds"
  },
  {
    title: "아라마키 요새",
    url: "/stages/sockeye-station/",
    description: "새먼 런 스테이지 - Sockeye Station"
  },
  {
    title: "무니 엘 해양 발전소",
    url: "/stages/gone-fission-hydroplant/",
    description: "새먼 런 스테이지 - Gone Fission Hydroplant"
  },
  {
    title: "난파선 돈 브라코",
    url: "/stages/marooners-bay/",
    description: "새먼 런 스테이지 - Marooner's Bay"
  },
  {
    title: "스지코 정션 터",
    url: "/stages/jammin-salmon-junction/",
    description: "새먼 런 스테이지 - Jammin' Salmon Junction"
  },
  {
    title: "토키라즈 이부시 공방",
    url: "/stages/salmonid-smokeyard/",
    description: "새먼 런 스테이지 - Salmonid Smokeyard"
  },
  {
    title: "돈피코 투기장",
    url: "/stages/bonerattle-arena/",
    description: "새먼 런 스테이지 - Bonerattle Arena"
  },
  {
    title: "거물 연어 공략",
    url: "/enemies/boss-salmon/",
    description: "폭탄, 어깨 패드, 철판, 뱀, 타워, 두더지, 박쥐, 기둥, 다이버, 냄비 뚜껑, 철 구슬 공략"
  },
  {
    title: "두목 연어 공략",
    url: "/enemies/boss-salmon/",
    description: "천하장사, 용, 죠 등 오카시라(두목) 연어 공략"
  },
  {
    title: "특수 상황 공략",
    url: "/special-situations/",
    description: "빛파리(러시), 안개, 그릴 발진, 운반함 급습, 진흙연어 분출, 거대 회오리 등 특수 웨이브"
  },
  {
    title: "무기 및 기어",
    url: "/weapons/",
    description: "새먼 런 지급 무기와 기어 정보"
  },
  {
    title: "빅 런 이벤트",
    url: "/events/",
    description: "빅 런, 팀 콘테스트 등 새먼 런 기간 한정 이벤트 정보"
  },
];

export function search(query: string): Array<{
  title: string;
  url: string;
  description: string;
}> {
  if (!query || query.trim().length === 0) {
    return [];
  }

  const lowerQuery = query.toLowerCase().trim();

 return searchIndex
    .filter((item) => {
      const titleMatch = item.title.toLowerCase().includes(lowerQuery);
      const descriptionMatch = item.description.toLowerCase().includes(lowerQuery);
      return titleMatch || descriptionMatch;
    })
    .sort((a, b) => {
      const aTitleMatch = a.title.toLowerCase().includes(lowerQuery);
      const bTitleMatch = b.title.toLowerCase().includes(lowerQuery);

      if (aTitleMatch && !bTitleMatch) return -1;
      if (!aTitleMatch && bTitleMatch) return 1;

      const aTitlePos = a.title.toLowerCase().indexOf(lowerQuery);
      const bTitlePos = b.title.toLowerCase().indexOf(lowerQuery);

      if (aTitlePos !== bTitlePos) {
        return aTitlePos - bTitlePos;
      }

      const aDescPos = a.description.toLowerCase().indexOf(lowerQuery);
      const bDescPos = b.description.toLowerCase().indexOf(lowerQuery);

      return aDescPos - bDescPos;
    });
}

if (typeof window !== 'undefined') {
  (window as any).salmonRunSearch = {
    search,
  };
}
