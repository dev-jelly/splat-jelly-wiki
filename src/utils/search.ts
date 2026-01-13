const searchIndex = [
  {
    title: "연어런 메인",
    url: "/salmon-run/",
    description: "스플래툰 3 연어런(연어런)의 전체 개요와 기본 정보"
  },
  {
    title: "스테이지 목록",
    url: "/salmon-run/stages/",
    description: "연어런의 모든 스테이지와 특징"
  },
  {
    title: "쇼어설 스크랩 야드",
    url: "/salmon-run/stages/shoreside-scrapyard/",
    description: "연어런 기본 스테이지 - 해변의 폐철지"
  },
  {
    title: "언더파스",
    url: "/salmon-run/stages/sockeye-station/",
    description: "연어런 기본 스테이지 - 지하철역"
  },
  {
    title: "해변 철길",
    url: "/salmon-run/stages/spawning-grounds/",
    description: "연어런 기본 스테이지 - 철길 정거장"
  },
  {
    title: "뉴 아메리칸 다운",
    url: "/salmon-run/stages/new-albacore-hotel/",
    description: "연어런 기본 스테이지 - 호텔 건물"
  },
  {
    title: "이글 레이크",
    url: "/salmon-run/stages/eeltail-alley/",
    description: "연어런 기본 스테이지 - 골목길"
  },
  {
    title: "마리나 스퀘어",
    url: "/salmon-run/stages/marina-bay/",
    description: "연어런 기본 스테이지 - 해변 상업 지구"
  },
  {
    title: "타이드 랜드",
    url: "/salmon-run/stages/tidal-wave-arena/",
    description: "연어런 기본 스테이지 - 콘서트 홀"
  },
  {
    title: "마호 마하이",
    url: "/salmon-run/stages/maho-mahi-resort/",
    description: "빅 런 스테이지 - 휴양지 리조트"
  },
  {
    title: "이루나 뷰",
    url: "/salmon-run/stages/undam-burger/",
    description: "빅 런 스테이지 - 햄버거 가게"
  },
  {
    title: "멍키 비치",
    url: "/salmon-run/stages/monkeys-beach/",
    description: "빅 런 스테이지 - 해변 휴양지"
  },
  {
    title: "글래티우스 밸리",
    url: "/salmon-run/stages/gluttones-valley/",
    description: "빅 런 스테이지 - 계곡 지역"
  },
  {
    title: "스태그웍스",
    url: "/salmon-run/stages/stageworks/",
    description: "빅 런 스테이지 - 공장 지역"
  },
  {
    title: "파밀리 벤드",
    url: "/salmon-run/stages/familys-bend/",
    description: "빅 런 스테이지 - 주거 지역"
  },
  {
    title: "적 종류",
    url: "/salmon-run/enemies/",
    description: "연어런의 모든 적 종류와 대처법"
  },
  {
    title: "자코 적",
    url: "/salmon-run/enemies/small-fry/",
    description: "연어런의 기본 적 - 자코 적"
  },
  {
    title: "보스 연어",
    url: "/salmon-run/enemies/boss-salmon/",
    description: "연어런의 보스 연어 종류와 대처법"
  },
  {
    title: "무기",
    url: "/salmon-run/weapons/",
    description: "연어런 무기 종류와 사용법"
  },
  {
    title: "특수 상황",
    url: "/salmon-run/special-situations/",
    description: "연어런 특수 상황 가이드"
  },
  {
    title: "이벤트",
    url: "/salmon-run/events/",
    description: "연어런 이벤트 가이드"
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
