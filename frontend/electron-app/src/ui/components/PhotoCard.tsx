import { useState, type ReactNode } from "react";
import { photoCardStyles } from "@/ui/styles/photoCardStyles";
import { ExternalLink } from "lucide-react";

type Props = {
    path: string;
    score: number;
    fileUrl: (p: string) => string;
    openPath: (p: string) => void;
};

export const PhotoCard = ({
    path,
    score,
    fileUrl,
    openPath,
}: Props): ReactNode => {
    const [isHovered, setIsHovered] = useState(false);
    const [isImgHovered, setIsImgHovered] = useState(false);
    console.log(score);
    return (
        <div
            style={{
                ...photoCardStyles.card,
                ...(isHovered && {
                    transform: "translateY(-4px)",
                    boxShadow: "0 12px 24px rgba(0, 0, 0, 0.1)",
                }),
            }}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
        >
            <div style={photoCardStyles.wrapper}>
                <img
                    src={fileUrl(path)}
                    alt={path}
                    style={{
                        ...photoCardStyles.img,
                        ...(isHovered && { transform: "scale(1.05)" }),
                    }}
                />
                <div
                    style={{
                        ...photoCardStyles.overlay,
                        ...(isHovered && { opacity: 1 }),
                    }}
                >
                    <button
                        style={{
                            ...photoCardStyles.openBtn,
                            ...(isImgHovered && { transform: "scale(1.1)" }),
                        }}
                        onClick={() => openPath(path)}
                        onMouseEnter={() => setIsImgHovered(true)}
                        onMouseLeave={() => setIsImgHovered(false)}
                    >
                        <ExternalLink size={18} />
                    </button>
                </div>
            </div>
            <div style={photoCardStyles.info}>
                <p style={photoCardStyles.path}>{path.split("/").pop()}</p>
                <span style={photoCardStyles.score}>
                    {(score * 100).toFixed(0)}% match
                </span>
            </div>
        </div>
    );
};
